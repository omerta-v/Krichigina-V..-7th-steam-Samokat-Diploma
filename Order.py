import requests
import Data
import Configuration

#Кричигина В. 7й Поток. Инженер по тестированию плюс. Финальный проект Яндекс.Самокат
#Creating new Order for track
def post_new_order(body):
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_ORDER,
                         json=body,
                         headers=Data.headers)  # а здесь заголовки

#Storing track into variable for convience
track = post_new_order(Data.order_body).json()["track"]
#Creating function for getting order data by track
def get_order_data(tracknumber):
    return requests.get(Configuration.URL_SERVICE + Configuration.GET_ORDER + str(tracknumber))

#Printing some values for cohesive debugging, comment them if not needed
print (track)
print (get_order_data(track))
print (get_order_data(""))
#Check Response Code for getting order Data with tracknumber
def positive_assert(trackorder):
    response = get_order_data(trackorder)
    assert response.status_code == 200
#Check Response Code for getting order Data without tracknumber
def negative_assert(trackorder):
    response = get_order_data(trackorder)
    assert response.status_code == 400
    assert response.json()["message"] == "Недостаточно данных для поиска"
#Tests:
#Checking response status code for order with track
def test_order_data_received():
    positive_assert(track)
#Checking response status code for order without track
def test_order_data_received_without_track():
    track=""
    negative_assert(track)