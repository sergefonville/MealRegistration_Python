app.controller('mealRegistrationController', ['$scope', '$http', function($scope, $http) {
  $scope.foodItems = [];
  $scope.units = [];
  $scope.units.push('Grams');
  $scope.units.push('Portions');
  $scope.addFoodItem = function() {
    var foodItem = {
      name: '',
      unit: $scope.units[0],
      amount: '',
      kcal: '',
      carbs: ''
    };
    $scope.foodItems.push(foodItem);
  };
  $scope.removeFoodItem = function(foodItem) {
    var foodItemIndex =  $scope.foodItems.indexOf(foodItem);
    $scope.foodItems.splice(foodItemIndex, 1);
  }
}]);
