(function ($, Backbone, _, config) {

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

    config.collections = {};
    
    config.collections.UploadCollection = Backbone.Collection.extend({
        model: Upload,
        url: config.api,
        parse: function (response) {
            this._count = response.count;
            return response.files || [];
        }
    });

})(jQuery, Backbone, _, config);
