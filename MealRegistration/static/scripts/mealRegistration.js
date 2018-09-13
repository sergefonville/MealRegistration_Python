var app = angular.module('mealRegistration', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'templates/main.template.html'
    })
    .when('/add', {
      templateUrl: 'templates/add.template.html'
    })
    .when('/show', {
      templateUrl: 'templates/show.template.html'
    })
    .when('/list', {
      templateUrl: 'templates/list.template.html'
    })
    .when('/edit', {
      templateUrl: 'templates/edit.template.html'
    });
  // This needs to be done as a function call, as a parameter to html5Mode does not work.
  $locationProvider.hashPrefix('');
}]);
