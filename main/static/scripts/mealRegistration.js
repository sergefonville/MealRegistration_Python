var app = angular.module('mealRegistration', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'views/main.html'
    })
    .when('/add', {
      templateUrl: 'views/add.html'
    })
    .when('/show', {
      templateUrl: 'views/show.html'
    })
    .when('/list', {
      templateUrl: 'views/list.html'
    })
    .when('/edit', {
      templateUrl: 'views/edit.html'
    });
  // This needs to be done as a function call, as a parameter to html5Mode does not work.
  $locationProvider.hashPrefix('');
}]);
