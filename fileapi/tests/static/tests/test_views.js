QUnit.test('Config Populated', function (assert) {
    assert.ok(config.views);
    assert.ok(config.views.UploadListingView);
    assert.ok(config.views.NewUploadView);
    assert.ok(config.views.LoginView);
});

QUnit.module('UploadListingView Tests', {
    beforeEach: function () {
        $('#qunit-fixture').append($('<div>', {id: 'files'}));
        this.view = new config.views.UploadListingView();
    },
    afterEach: function () {
        this.view.remove();
    }
});

QUnit.test('Add Upload', function (assert) {
    var uploads = new config.collections.UploadCollection(),
        upload = uploads.push({
            name: 'test.png',
            size: 200,
            created: '2015-01-14T01:21:56.870',
            links: {
                self: '/uploads/test.png'
            }
        });
    this.view.addFile(upload);
    assert.equal($('.file', this.view.$el).length, 1);
});
