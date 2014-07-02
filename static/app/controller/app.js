val app = angular.module('djangoApp', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

app.controller('HelloController', function($scope) {
  var someText = {};
  someText.message = 'You are started your app';
  $scope.someText = someText;
});

