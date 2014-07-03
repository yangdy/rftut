var djangoApp = angular.module('djangoApp', []);

djangoApp.controller('HelloController', function($scope) {
  var message = {};
  message.greeting = 'hello, angularjs!';
  $scope.message = message;
});
