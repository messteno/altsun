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
