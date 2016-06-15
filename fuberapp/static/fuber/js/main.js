app.controller("CabsCtrl",function($scope, $state, 
    $timeout, APIService, $log) {

    $scope.fetchCabs = function(){
        var params = {}
        var end_point = "/api/cabs"
        APIService.getRequest(end_point, params, null)
        .success(function(data) {
            $scope.cabs  = data
        }).error(function(data){
            
        });
    }

    $scope.getBookingHistory = function(){
        var params = {}
        var end_point = "/api/booking/history"
        APIService.getRequest(end_point, params, null)
        .success(function(data) {
            for (var i = 0; i < data.length; i++) {
                data[i].pickup_time = Date.parse(data[i].start_time)
            };
            $scope.bookings  = data
        }).error(function(data){
            
        });
    }

    $scope.getLocation = function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(getPosition);
        } else {
            alert("Geolocation is not supported by this browser.")
        }
    }

    function getPosition(position) {
        $scope.position = {latitude:position.coords.latitude, longitude:position.coords.longitude}
    }

    $scope.fetchCabs()
    $scope.getBookingHistory()
    $scope.getLocation()

    $scope.start_trip = function(){
        var end_point = "/api/start/trip"
        var payload = angular.copy($scope.position)
        APIService.postRequest(end_point, payload, null)
        .success(function(data) {
            if (data.trip){
                for (var i = 0; i < $scope.cabs.length; i++) {
                    if($scope.cabs[i].id == data.trip.cab.id){
                        $scope.cabs.splice(i, 1);
                        break;
                    }
                };
            
                data.trip.pickup_time = Date.parse(data.trip.start_time)
                $scope.bookings.unshift(data.trip)
                alert("trip started")
            }
            else{
                alert("No cabs available")
            }
        }).error(function(data){
            alert(JSON.stringify(data))
        });
    }

    $scope.end_trip = function(trip){
        var end_point = "/api/end/trip/"+trip.id
        var payload = angular.copy($scope.position)
        APIService.postRequest(end_point, payload, null)
        .success(function(data) {
            trip.fare = data.fare
            trip.is_running = false
            trip.cab.is_assigned = false
            $scope.cabs.unshift(angular.copy(trip.cab))
        }).error(function(data){
            alert(JSON.stringify(data))
        });
    }


});