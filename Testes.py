import requests
from datetime import datetime

def lambda_handler(event, context):
    # TODO: Implement attempts
    uri_pagarme = 'https://api.pagar.me/1/'
    uri_track_cash = 'https://sistema.trackcash.com.br/api/mkp/'

    auth_pagarme = {
        'api_key': event['auth']['api_key']
    }

    def logging(event, level, message, context):
        if not message.strip() and not context:
            return

        if 'logging' not in event:
            event['logging'] = {
                'logs': []
            }

        event['logging']['logs'].append({
            'service': 'sls-api-zoom',
            'level': level,
            'message': message,
            'context': context,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def catch_response_error(event, message, response=None):
        event['attempts'] = event.get('attempts', 0) + 1

        event['message'] = message
        event['status'] = False
        event['code'] = 400

        params = {}
        if response:
            params = {
                'statusCode': response.get_http_status_code(),
                'message': response.get_error_message(),
                'body': response.get_response()
            }

        event['params'] = params

        logging(event, 'notice', message, {
            'account': event.get('account', None),
            'store': event.get('id_store', None),
            'request': {
                'statusCode': params.get('statusCode', None),
                'message': params.get('message', None),
            }
        })

        return {'body': event}

    def response_success(event, message, response=None):
        event['message'] = message
        event['status'] = True
        event['code'] = 200

        params = {}
        if response:
            params = {
                'statusCode': response.get_http_status_code(),
                'message': response.get_error_message(),
                'body': response.get_response()
            }

        event['params'] = params

        return {'body': event}

    def get(url, request):
        curl = requests.get(url, params=request, headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        return curl

    def post(url, request):
        curl = requests.post(url, json=request, headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'token': getenv('TRACKCASH_TOKEN')})

        return curl

    def date_format(value, hora=True):
        if not value:
            return None

        if not hora:
            return datetime.strptime(value.replace('/', '-'), '%Y-%m-%d').strftime('%Y-%m-%d')
        else:
            return datetime.strptime(value.replace('/', '-'), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

    # Other functions remain unchanged

    id_store = event['id_store']
    id_account = event['account']

    filters = set_filters(event)

    request_pagarme = {**filters, **auth_pagarme}

    response_pagarme = get(uri_pagarme + ('payables' if event['job'] == '4002' or event['job'] == '4003' else 'transactions'), request_pagarme)

    if response_pagarme.status_code != 200:
        return catch_response_error(event, 'Ocorreu um erro na comunicação com a Pagarme', response_pagarme)

    request = []
    body_pagarme = response_pagarme.json()

    for item in body_pagarme:
        if event['job'] == '4002' or event['job'] == '4003':
            # Rest of the code for this block remains unchanged
            pass
        else:
            id_status = get_status_id(item['status'])
            reference = get_references(item)

            request.append({
                'id_store': id_store,
                'id_channel': 143,
                'id_account': id_account,
                'id_order': item['id'],
                'reference': reference or item['id'],
                'original_status': item['status'],
                'id_status': id_status,
                'date': date_format(item['date_created']),
                'payments': [{
                    'payment_id': item['id'],
                    'payment_method': 143,
                    'payment_service': get_payment_service_id(item['payment_method'], item.get('installments', 1) > 1),
                    'payment_brand': get_payment_brand_id(item.get('card_brand'), item['payment_method']),
                    'payment_installments': item.get('installments', 1),
                    'payment_status': id_status,
                    'payment_total': item['amount'],
                    'payment_total_discount': item['discount'],
                    'payment_total_fee': item['cost'],
                    'payment_total_rate': item['paid_amount'] - item['amount'] if item['paid_amount'] != 0 else 0,
                    'payment_due_date': date_format(item['date_created']),
                    'payment_confirmed_date': date_format(item['date_created']),
                }],
            })

    if request:
        response_track_cash = post(uri_track_cash + ('payments' if event['job'] == '4002' or event['job'] == '4003' else 'orders'), request)

        if response_track_cash.status_code != 200:
            return catch_response_error(event, 'Ocorreu um erro na comunicação com a TrackCash', response_track_cash)

        meta = check_for_more(request_pagarme)

        return response_next_page(event, meta)

    return response_success(event, 'Nenhum item para enviar')
