import requests

session_booking = requests.session()

url_booking = 'https://restful-booker.herokuapp.com/booking'
headers = {'Content-Type': 'application/json',}

json_data = {
    'firstname': 'Ruby',
    'lastname': 'Brown',
    'totalprice': 1025,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
}

#Авторизация для получения токена
json_data_admin = {
    'username': 'admin',
    'password': 'password123',
}

response_admin = requests.post('https://restful-booker.herokuapp.com/auth', headers=headers, json=json_data_admin)
token = response_admin.json()['token']


#Создание бронирования
booking_room = session_booking.post(url_booking, headers=headers, json=json_data)

#Изменение даты заезда
cookies = {'token': token}
json_data_new = {
    'bookingdates': {
        'checkin': '2018-05-05',
        'checkout': '2019-01-01',
    },
}

req = session_booking.get(url_booking+'?firstname=Ruby&lastname=Brown')
id_booking = req.json()[0]["bookingid"]

change_booking = session_booking.patch(url_booking+'/'+str(id_booking), cookies=cookies, headers=headers, json=json_data_new)
#Печать созданного бронирования
for key, value in change_booking.json().items():
    print(key, '-', value)

#Удаление созданного бронирования
response_delete = session_booking.delete(url_booking+'/'+str(id_booking), cookies=cookies, headers=headers)

#Проверка оставшихся бронирований
check_booking = session_booking.get(url_booking+'/'+str(id_booking), headers=headers, json=json_data)

try:
    print(check_booking.json())
    print('Booking was not deleted')
except requests.exceptions.JSONDecodeError:
    print('Booking was deleted')
