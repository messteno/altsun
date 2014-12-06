'use strict';

var Profile = function(djResource, $http) {
    var Profile = djResource('/api/profile/');
    Profile.prototype.$logout = function(success) {
        $http.get('/api/logout/')
            .success(function(request) {
                if(success) {
                    success();
                }
            })
            .error(function(request) {
            });
    };
    return Profile;
};

var News = function(djResource) {
    var News = djResource('/api/news/:newsId/',
                          {newsId: '@newsId', count: '@count', page: '@page'});
    return News;
};

var NewsItem = function(djResource) {
    var NewsItem = djResource('/api/news/item/:newsId/',
                              {newsId: '@newsId'});
    return NewsItem;
};

var Releases = function(djResource) {
    var Releases = djResource('/api/releases/:releaseId/',
                          {releaseId: '@releaseId', count: '@count', page: '@page',
                           podcast: '@podcast'});
    return Releases;
};

var ReleasesItem = function(djResource) {
    var ReleasesItem = djResource('/api/releases/item/:releaseId/',
                                  {releaseId: '@releaseId'});
    return ReleasesItem;
};

var Artists = function(djResource) {
    var Artists = djResource('/api/artists/:artistId/',
                          {artistId: '@artistId', count: '@count', page: '@page'});
    return Artists;
};

var ArtistsItem = function(djResource) {
    var ArtistsItem = djResource('/api/artists/item/:artistId/',
                                  {artistId: '@artistId'});
    return ArtistsItem;
};

var Form = function($cookies, $http) {
    var Form = function($scope, processLink, successCallback, errorCallback) {
        this.disabled = false;
        this.data = {};
        this.error = {};
        this.focus = {};
        this.method = 'POST';
        this.processLink = processLink;
        this.success = false;

        this.submit = function(params) {
            if (!this.processLink)
                return false;

            if (this.beforeSubmit)
                this.beforeSubmit(params);

            if (!this.data)
                return false;

            var self = this;
            self.disabled = true;
            
            $http({
                method: self.method,
                url: self.processLink,
                data: self.data,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': $cookies.csrftoken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                cache: false,
                transformResponse: function (data, headersGetter) {
                    try {
                        var jsonObject = JSON.parse(data);
                        return jsonObject;
                    } catch (e) {
                    }
                    return {};
                }
            })
            .success(function(data, status) {
                self.success = true;
                self.error = {};
                self.focus = {};
                self.data = {};
                if (successCallback) {
                    successCallback(data, params);
                }
                self.disabled = false;
            })
            .error(function(data) {
                var firstFocusKey = Object.keys(self.focus)[0];
                self.focus = {};
                self.error = {};
                self.success = false;

                try {
                    for(var key in data) {
                        if (Object.keys(self.focus).length == 0 || key === firstFocusKey) {
                            self.focus = {};
                            self.focus[key] = true;
                        }
                        self.error[key] = data[key][0];
                    }
                } catch(e) {
                    self.focus[firstFocusKey] = true;
                    self.error['__all__'] = 'Ошибка при обработке формы';
                }
                if (Object.keys(self.error).length == 0) {
                    self.focus[firstFocusKey] = true;
                    self.error['__all__'] = 'Ошибка при обработке формы';
                }

                if (self.focus.__all__ != undefined) {
                    self.focus[Object.keys(self.data)[0]] = self.focus.__all__;
                    delete self.focus.__all__;
                }

                if (errorCallback) {
                    errorCallback(data, params);
                }

                self.disabled = false;
            });
        };

        this.closeAlert = function(name) {
            delete this.error[name];
        };

        this.isSuccess = function() {
            return this.success;
        };
    };
    return Form;
};

angular
    .module('altsunServices', ['ngResource'])
    .factory('Profile', Profile)
    .factory('News', News)
    .factory('NewsItem', NewsItem)
    .factory('Releases', Releases)
    .factory('ReleasesItem', ReleasesItem)
    .factory('Artists', Artists)
    .factory('ArtistsItem', ArtistsItem)
    .factory('Form', Form);

