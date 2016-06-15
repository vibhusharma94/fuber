app.service('APIService', ['$http', function($http) {

        var _postRequest = function(endPoint, data, headers) {
            var url = endPoint
            var config = {headers:  headers};
            return $http.post(url, data, config)
        };

        var _putRequest = function(endPoint, data, headers) {
            var url = endPoint
            var config = {headers:  headers};
            return $http.put(url, data, config)
        };

        var _getRequest = function(endPoint, params, headers) {
            var url = endPoint
            if (params && Object.keys(params).length > 0) {
                url = url + '?';
                for (var key in params) {
                  if (params.hasOwnProperty(key)) {
                    url = url + key + '=' + params[key] + '&';   
                  }
                }
            };

            var config = {headers:  headers
            };
            return $http.get(url,config)
        }

        var _deleteRequest = function(endPoint, params, headers) {
            var url = endPoint
            if (params && Object.keys(params).length > 0) {
                url = url + '?';
                for (var key in params) {
                  if (params.hasOwnProperty(key)) {
                    url = url + key + '=' + params[key] + '&';   
                  }
                }
            };

            var config = {headers:  headers
            };
            return $http.delete(url,config)
        }

        return {
            getRequest: _getRequest,
            postRequest: _postRequest,
            putRequest:_putRequest,
            deleteRequest:_deleteRequest,
        };
}]);