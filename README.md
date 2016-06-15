Fuber App
===================================================================

1. Dev tools Installations
	* sudo apt-get install build-essential python-dev libevent-dev libxml2-dev libmysqlclient-dev python-setuptools python-pip libpq-dev libxslt1-dev

2. Install Mysql
    * sudo apt-get install mysql-server
    * mysql -u root -p
    * create database fuberdb;
    * sudo service mysql start
    * sudo service mysql stop
   
3. Install Virtualenv
    * pip install virtualenv

4. Virtualenv Setup
    * virtualenv env
    * source bin/activate
    * deactivate

5. Install requirements
    * pip install -r requirements.txt 

6. create tables
   * python manage.py migrate

7. Start Django test server
   * python manage.py runserver 8000
   
8. Test django app
   * python manage.py test apps.apis.fuber -k -v 3


 Rest API Documentation
-----------------------------

#### **Start Trip**


    http://127.0.0.1:8000/api/start/trip

##### **POST**

*Request*

    #!shell
    curl -X POST -H "Content-Type: application/json" -d '{
    "latitude":12.9399438,
    "longitude":77.626416
    }' "http://127.0.0.1:8000/api/start/trip"


*Response*
```
#!json
{
  "id": 2,
  "cab": {
    "id": 3,
    "number": 3456,
    "cab_type": "fuberX",
    "color": "white",
    "latitude": 12.9403994,
    "longitude": 77.6249732,
    "is_assigned": true,
    "created": "2016-06-15T13:00:51.275527Z"
  },
  "fare": 0,
  "customer_name": "vibhu",
  "start_time": "2016-06-15T16:05:48.294319",
  "end_time": null,
  "start_latitude": 12.9403994,
  "start_longitude": 77.6249732,
  "end_latitude": null,
  "end_longitude": null,
  "is_running": true
}
```
         
#### **End Trip**
    
    http://127.0.0.1:8000/api/end/trip/<booking_id>
    
#####  **GET**

##### **Descrpition**

     End Trip and calculate fare based on distance, time and cab color

*Request*

    #!shell
    curl -X POST -H "Content-Type: application/json" -d '{
    "latitude":12.9668035,
    "longitude":77.6511922
    }' "http://127.0.0.1:8000/api/end/trip/2"
    
```
#!json
{
  "id": 8,
  "cab": {
    "id": 4,
    "driver_name": "Travis Kalanick",
    "number": 8765,
    "cab_type": "fuberXL",
    "color": "pink",
    "latitude": 12.9668035,
    "longitude": 77.6511922,
    "is_assigned": false,
    "created": "2016-06-15T13:01:27.057420"
  },
  "fare": 89,
  "start_time": "2016-06-15T18:45:17.666573",
  "end_time": "2016-06-15T20:01:06.102212",
  "start_latitude": 12.9383499,
  "start_longitude": 77.6180639,
  "end_latitude": 12.9668035,
  "end_longitude": 77.6511922,
  "is_running": false
}
```

#### **Get Available cabs**
    
    http://127.0.0.1:8000/api/cabs
    
#####  **GET**

*Request*

    #!shell
    curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8000/api/cabs"

```
#!json
[
  {
    "id": 2,
    "number": 1234,
    "cab_type": "fuberGo",
    "color": "black",
    "latitude": 12.9403994,
    "longitude": 77.6249732,
    "is_assigned": false,
    "created": "2016-06-15T13:00:12.816104"
  },
  {
    "id": 3,
    "number": 3456,
    "cab_type": "fuberX",
    "color": "white",
    "latitude": 12.9668035,
    "longitude": 77.6511922,
    "is_assigned": false,
    "created": "2016-06-15T13:00:51.275527"
  },
  {
    "id": 4,
    "number": 8765,
    "cab_type": "fuberXL",
    "color": "pink",
    "latitude": 12.9383499,
    "longitude": 77.6180639,
    "is_assigned": false,
    "created": "2016-06-15T13:01:27.057420"
  },
  {
    "id": 5,
    "number": 4325,
    "cab_type": "fuberGo",
    "color": "black",
    "latitude": 12.9572963,
    "longitude": 77.6271619,
    "is_assigned": false,
    "created": "2016-06-15T13:02:14.189042"
  }
]

```    


#### **Cab Booking History**
    
    http://127.0.0.1:8000/api/booking/history
    
#####  **GET**

*Request*

    #!shell
    curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8000/api/booking/history"

```
#!json
[
  
  {
    "id": 9,
    "cab": {
      "id": 5,
      "driver_name": "Travis Kalanick",
      "number": 4325,
      "cab_type": "fuberGo",
      "color": "black",
      "latitude": 12.9572963,
      "longitude": 77.6271619,
      "is_assigned": true,
      "created": "2016-06-15T13:02:14.189042"
    },
    "fare": 0,
    "start_time": "2016-06-15T18:45:24.936489",
    "end_time": null,
    "start_latitude": 12.9572963,
    "start_longitude": 77.6271619,
    "end_latitude": null,
    "end_longitude": null,
    "is_running": true
  },
  {
    "id": 8,
    "cab": {
      "id": 4,
      "driver_name": "Travis Kalanick",
      "number": 8765,
      "cab_type": "fuberXL",
      "color": "pink",
      "latitude": 12.9668035,
      "longitude": 77.6511922,
      "is_assigned": false,
      "created": "2016-06-15T13:01:27.057420"
    },
    "fare": 89,
    "start_time": "2016-06-15T18:45:17.666573",
    "end_time": "2016-06-15T20:01:06.102212",
    "start_latitude": 12.9383499,
    "start_longitude": 77.6180639,
    "end_latitude": 12.9668035,
    "end_longitude": 77.6511922,
    "is_running": false
  },
  {
    "id": 7,
    "cab": {
      "id": 2,
      "driver_name": "Travis Kalanick",
      "number": 1234,
      "cab_type": "fuberGo",
      "color": "black",
      "latitude": 12.9396099,
      "longitude": 77.6264524,
      "is_assigned": true,
      "created": "2016-06-15T13:00:12.816104"
    },
    "fare": 0,
    "start_time": "2016-06-15T18:45:14.635239",
    "end_time": null,
    "start_latitude": 12.9396099,
    "start_longitude": 77.6264524,
    "end_latitude": null,
    "end_longitude": null,
    "is_running": true
  },
  {
    "id": 6,
    "cab": {
      "id": 2,
      "driver_name": "Travis Kalanick",
      "number": 1234,
      "cab_type": "fuberGo",
      "color": "black",
      "latitude": 12.9396099,
      "longitude": 77.6264524,
      "is_assigned": true,
      "created": "2016-06-15T13:00:12.816104"
    },
    "fare": 5,
    "start_time": "2016-06-15T18:44:48.171940",
    "end_time": "2016-06-15T18:44:56.893777",
    "start_latitude": 12.9395955,
    "start_longitude": 77.6264548,
    "end_latitude": 12.9396099,
    "end_longitude": 77.6264524,
    "is_running": false
  },
]

```    
