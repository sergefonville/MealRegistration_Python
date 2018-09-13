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
      kcalUnit: '',
      carbsUnit: '',
      kcals: '',
      carbs: ''
    };
    $scope.foodItems.push(foodItem);
    $scope.recalculate = function() {
      if($scope.amount > 0 && $scope.kcalUnit > 0 && $scope.carbsUnit > 0) {
        switch($scope.unit) {
          case 'Grams':
            $scope.kcal = $scope.amount * $scope.kcalsUnit / 100;
            $scope.carbs = $scope.amount * $scope.carbsUnit / 100;
            break;
          case 'Portions':
            $scope.kcal = $scope.amount * $scope.kcalsUnit;
            $scope.carbs = $scope.amount * $scope.carbsUnit;
            break;
        }
      }
    }
  };
  $scope.removeFoodItem = function(foodItem) {
    var foodItemIndex =  $scope.foodItems.indexOf(foodItem);
    $scope.foodItems.splice(foodItemIndex, 1);
  }
}]);
