'use strict';

app.controller('MainCtrl', function($scope, $modal, $window, $location, $sce, loader, Profile, News, Releases) {
    // $scope.loader = loader;
    $scope.profile = Profile.get();

    $scope.logout = function() {
        $scope.profile.$logout(function() {
            $location.path('/');
            $scope.$apply();
            $window.location.reload();
        });
    };

    $scope.login = function() {
        var modalInstance = $modal.open({
            templateUrl: '/static/mesteno/login.html',
            controller: 'LoginModalCtrl',
            windowClass: 'login-modal',
            scope: $scope,
        });
    };

    $scope.news = News.get({page: 1, count: 2});
    $scope.releases = Releases.get({page: 1, count: 4}, function() {
        for (var i = 0; i < $scope.releases.results.length; i++) {
            var release = $scope.releases.results[i];
            release.embed = $sce.trustAsHtml(release.embed);
            if (release.podcast) {
                release.link = '/#/releases/' + release.id;
            } else {
                release.link = '/#/podcasts/' + release.id;
            }
        }
    });
});

app.controller('NewsCtrl', function($scope, News) {
    $scope.news = News.query();
});

app.controller('NewsItemCtrl', function($scope, $stateParams, $state, NewsItem) {
    $scope.news = NewsItem.get({newsId: $stateParams.newsId}, function() {
    }, function() {
        $state.go('404');
    });
});

app.controller('ReleasesCtrl', function($scope, $sce, Releases) {
    $scope.releases = Releases.query({podcast: 'False'}, function() {
        for (var i = 0; i < $scope.releases.length; i++) {
            $scope.releases[i].embed = $sce.trustAsHtml($scope.releases[i].embed);
        }
    });
});

app.controller('ReleasesItemCtrl', function($scope, $state, $stateParams, $sce, ReleasesItem) {
    $scope.release = ReleasesItem.get({releaseId: $stateParams.releaseId}, function() {
        $scope.release.embed = $sce.trustAsHtml($scope.release.embed);
        for (var i = 0; i < $scope.release.neigbours.length; i++) {
            $scope.release.neigbours[i].embed = $sce.trustAsHtml($scope.release.neigbours[i].embed);
        }
    }, function() {
        $state.go('404');
    });
});

app.controller('PodcastsCtrl', function($scope, $sce, Releases) {
    $scope.releases = Releases.query({podcast: 'True'}, function() {
        for (var i = 0; i < $scope.releases.length; i++) {
            $scope.releases[i].embed = $sce.trustAsHtml($scope.releases[i].embed);
        }
    });
});

app.controller('PodcastsItemCtrl', function($scope, $stateParams, $sce, ReleasesItem) {
    $scope.release = ReleasesItem.get({releaseId: $stateParams.podcastId}, function() {
        $scope.release.embed = $sce.trustAsHtml($scope.release.embed);
        for (var i = 0; i < $scope.release.neigbours.length; i++) {
            $scope.release.neigbours[i].embed = $sce.trustAsHtml($scope.release.neigbours[i].embed);
        }
    }, function() {
        $state.go('404');
    });
});

app.controller('ArtistsCtrl', function($scope, Artists) {
    $scope.artists = Artists.query();
});

app.controller('ArtistsItemCtrl', function($scope, $stateParams, $sce, ArtistsItem) {
    $scope.artist = ArtistsItem.get({artistId: $stateParams.artistId}, function() {
        for (var i = 0; i < $scope.artist.releases.length; i++) {
            var release = $scope.artist.releases[i];
            release.embed = $sce.trustAsHtml(release.embed);
            if (release.podcast) {
                release.link = '/#/releases/' + release.id;
            } else {
                release.link = '/#/podcasts/' + release.id;
            }
        }
    }, function() {
        $state.go('404');
    });
});

