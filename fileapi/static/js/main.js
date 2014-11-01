(function ($, Backbone, _) {

    var Upload = Backbone.Model.extend({
        url: function () {
            var links = this.get('links'),
                url = links && links.self;
            if (!url) {
                url = Backbone.Model.prototype.url.call(this);
            }
            return url;
        },
        idAttribute: 'name'
    });
    
    var UploadCollection = Backbone.Collection.extend({
        model: Upload,
        url: '/uploads/',
        parse: function (response) {
            this._count = response.count;
            return response.files || [];
        }
    });

    var uploads = new UploadCollection();

    var UploadView = Backbone.View.extend({
        className: 'file',
        template: _.template('<%- name %> <a class="delete" href="#">X</a>'),
        events: {
            'click .delete': 'delete'
        },
        initialize: function() {
            this.listenTo(this.model, 'change', this.render);
            this.listenTo(this.model, 'destroy', this.remove);
        },
        render: function () {
            this.$el.html(this.template(this.model.toJSON()));
        },
        delete: function (e) {
            e.preventDefault();
            this.model.destroy();
        }
    });

    var UploadListingView = Backbone.View.extend({
        el: '#files',
        render: function () {
            this.$el.show();
        },
        addFile: function (file) {
            var view = new UploadView({model: file});
            this.$el.append(view.$el);
            view.render();
        }
    });

    var NewUploadView = Backbone.View.extend({
        el: '#upload',
        events: {
            'dragenter': 'enter',
            'dragover': 'over',
            'dragend': 'end',
            'dragleave': 'end',
            'drop': 'drop'
        },
        enter: function (e) {
            e.stopPropagation();
            e.preventDefault();
            this.$el.addClass('hover');
            return false;
        },
        over: function (e) {
            e.stopPropagation();
            e.preventDefault();
            this.$el.addClass('hover');
            return false;
        },
        end: function (e) {
            this.$el.removeClass('hover');
        },
        drop: function (e) {
            var formData = new FormData(),
                file;
            e.stopPropagation();
            e.preventDefault();
            if (e.originalEvent.dataTransfer.files.length === 0) {
                return;
            }
            file = e.originalEvent.dataTransfer.files[0];
            formData.append('name', file);
            uploads.create({}, {
                error: $.proxy(this.fail, this),
                wait: true,
                data: formData,
                processData: false,
                contentType: false
            });
            this.end();
        },
        fail: function (_model, response) {
            var errors = response.responseJSON.name,
                errorTemplate = _.template('<p class="error error-<%- code %>"><%- message %></p>');
            _.map(errors, function (error) {
                this.$el.before(errorTemplate(error));
            }, this);
            setTimeout($.proxy(function() {
                var errors = $('.error');
                errors.fadeOut('slow', function () {
                    errors.remove();
                });
            }, this), 2500);
        },
        render: function () {
            this.$el.show();
        }
    });

    var LoginView = Backbone.View.extend({
        el: '#login',
        events: {
            'submit': 'submit'
        },
        submit: function (e) {
            e.preventDefault();
            var data = JSON.stringify({
                username: $(':input[name="username"]', this.$el).val(),
                password: $(':input[name="password"]', this.$el).val(),
            });
            $('.error', this.$el).remove();
            $.post('/api-token/', data)
                .done($.proxy(this.login, this))
                .fail($.proxy(this.fail, this));
        },
        login: function (result) {
            this.trigger('login', result.token);
            this.$el.hide();
        },
        fail: function () {
            this.$el.prepend('<p class="error">Invalid username/password</p>');
        }
    });

    var listView = new UploadListingView(),
        newView = new NewUploadView(),
        loginView = new LoginView();

    uploads.on('add', listView.addFile, listView);
    loginView.on('login', function (token) {
        $.ajaxPrefilter(function (settings, options, xhr) {
            xhr.setRequestHeader('Authorization', 'Bearer ' + token);
        });
        newView.render();
        listView.render();
        uploads.fetch();
    });

})(jQuery, Backbone, _);
