var config = (function ($, Backbone, _) {

    $(document).ready(function () {
        var uploads = new config.collections.UploadCollection(),
            listView = new config.views.UploadListingView(),
            newView = new config.views.NewUploadView({uploads: uploads}),
            loginView = new config.views.LoginView();

        uploads.on('add', listView.addFile, listView);
        loginView.on('login', function (token) {
            $.ajaxPrefilter(function (settings, options, xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            });
            newView.render();
            listView.render();
            uploads.fetch();
        });
    });

    return JSON.parse($('#config').text());

})(jQuery, Backbone, _);
