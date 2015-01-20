'use strict';

var baseSettings = function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    $httpProvider.defaults.transformRequest = [function(data) {
        var param = function(obj) {
            var query = '';
            var name, value, fullSubName, subName, subValue, innerObj, i;

            for (name in obj) {
                value = obj[name];

                if (value instanceof Array) {
                    for (i = 0; i < value.length; ++i) {
                        subValue = value[i];
                        fullSubName = name + '[' + i + ']';
                        innerObj = {};
                        innerObj[fullSubName] = subValue;
                        query += param(innerObj) + '&';
                    }
                } else if (value instanceof Object) {
                    for (subName in value) {
                        subValue = value[subName];
                        fullSubName = name + '[' + subName + ']';
                        innerObj = {};
                        innerObj[fullSubName] = subValue;
                        query += param(innerObj) + '&';
                    }
                } else if (value !== undefined && value !== null) {
                    query += encodeURIComponent(name) + '=' + encodeURIComponent(value) + '&';
                }
            }
            return query.length ? query.substr(0, query.length - 1) : query;
        };
        return angular.isObject(data) && String(data) !== '[object File]' ? param(data) : data;
    }];
};

var routerSettings = function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider
        .when('', '/main')
        .when('/', '/main')
        .otherwise('/404')
        ; 

    $stateProvider
        .state('404', {
            url: '/404',
            templateUrl: '/static/altsun/404.html',
        })
        .state('main', {
            url: '/main',
            templateUrl: '/static/altsun/main.html',
        })
        .state('news', {
            url: '/news',
            templateUrl: '/static/altsun/news/index.html',
            controller: 'NewsCtrl',
        })
        .state('news.item', {
            url: '/{newsId:[0-9]+}',
            templateUrl: '/static/altsun/news/item.html',
            controller: 'NewsItemCtrl',
        })
        .state('releases', {
            url: '/releases',
            templateUrl: '/static/altsun/releases/index.html',
            controller: 'ReleasesCtrl',
        })
        .state('releases.item', {
            url: '/{releaseId:[0-9]+}',
            templateUrl: '/static/altsun/releases/item.html',
            controller: 'ReleasesItemCtrl',
        })
        .state('podcasts', {
            url: '/podcasts',
            templateUrl: '/static/altsun/podcasts/index.html',
            controller: 'PodcastsCtrl',
        })
        .state('podcasts.item', {
            url: '/{podcastId:[0-9]+}',
            templateUrl: '/static/altsun/podcasts/item.html',
            controller: 'PodcastsItemCtrl',
        })
        .state('artists', {
            url: '/artists',
            templateUrl: '/static/altsun/artists/index.html',
            controller: 'ArtistsCtrl',
        })
        .state('artists.item', {
            url: '/{artistId:[0-9]+}',
            templateUrl: '/static/altsun/artists/item.html',
            controller: 'ArtistsItemCtrl',
        })
        .state('about', {
            url: '/about',
            templateUrl: '/static/altsun/about.html',
        })
        ;

};

var app = angular
    .module('altsun', [
        'ngRoute',
        'ngResource',
        'ngCookies',
        'ngAnimate',
        'ngSanitize',
        'djangoRESTResources',
        'altsunServices',
        'angular-loading-bar',
        'ui.bootstrap',
        'ui.router',
    ])
    .config(baseSettings)
    .config(routerSettings)
    .value('loader', {show: false});
