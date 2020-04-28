import requests
import json
import settings

api_access_token = settings.api_qiwi_token
mylogin = settings.qiwi_login


# Профиль пользователя
def get_profile(api_access_token):
    s7 = requests.Session()
    s7.headers['Accept'] = 'application/json'
    s7.headers['authorization'] = 'Bearer ' + api_access_token
    p = s7.get(
        'https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    return p.json()


# Полная информация о профиле пользователя
profile = get_profile(api_access_token)


# История платежей - последние и следующие n платежей
def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    return h.json()


def get_payment(user_telegram_id):
    last_payments = payment_history_last(mylogin, api_access_token, 10, '', '')
    payments = last_payments.get('data')
    for payment in payments:
        comment = payment.get('comment')
        if comment == str(user_telegram_id):
            payment_sum = payment.get('sum')
            payment_sum_amount = payment_sum.get('amount')
            return payment_sum_amount

# if __name__ == "__main__":
#     get_payment(user_telegram_id)
