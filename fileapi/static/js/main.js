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

})(jQuery, Backbone, _);
