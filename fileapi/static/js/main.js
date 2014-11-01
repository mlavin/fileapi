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
        template: _.template('<%- name %>'),
        initialize: function () {
            this.listenTo(this.model, 'change', this.render);
            this.listenTo(this.model, 'destroy', this.remove);
        },
        render: function () {
            this.$el.html(this.template(this.model.toJSON()));
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

    var listView = new UploadListingView();
    uploads.on('add', listView.addFile, listView);
    uploads.fetch();
    listView.render();

})(jQuery, Backbone, _);
