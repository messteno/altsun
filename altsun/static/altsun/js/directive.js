'use strict';

app.directive('owlCarousel', function () {  
    return {  
        restrict: 'E',  
        link: function (scope, element, attrs) {  
            $(element).owlCarousel({
                autoPlay: 5000,
                stopOnHover: true,  
                slideSpeed: 300,
                paginationSpeed: 400,
                singleItem: true
            });
        }  
    };  
});

app.directive('focusMe', function($timeout, $parse) {
    return {
        link: function(scope, element, attrs) {
            var model = $parse(attrs.focusMe);
            scope.$watch(model, function(value) {
                if(value === true) { 
                    $timeout(function() {
                        element[0].focus(); 
                    });
                }
            });
            element.bind('blur', function() {
                scope.$apply(model.assign(scope, false));
            })
        }
    };
});

app.directive('disableAnimation', function($animate){
    return {
        restrict: 'A',
        link: function($scope, $element, $attrs){
            $attrs.$observe('disableAnimation', function(value){
                $animate.enabled(!value, $element);
            });
        }
    }
});
