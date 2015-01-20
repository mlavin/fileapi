QUnit.test('Config Populated', function (assert) {
    assert.ok(config.collections);
    assert.ok(config.collections.UploadCollection);
});

QUnit.test('Parse Empty API response', function (assert) {
    var uploads = new config.collections.UploadCollection(),
        response = {
            count: 0,
            files: []
        };
    assert.deepEqual(uploads.parse(response), []);
});

QUnit.test('Parse Populated API response', function (assert) {
    var uploads = new config.collections.UploadCollection(),
        file = {
            name: 'test.png',
            size: 200,
            created: '2015-01-14T01:21:56.870',
            links: {
                self: '/uploads/test.png'
            }
        },
        response = {
            count: 1,
            files: [file]
        };
    assert.deepEqual(uploads.parse(response), [file]);
});

QUnit.test('Model Provided URL', function (assert) {
    var uploads = new config.collections.UploadCollection(),
        file = {
            name: 'test.png',
            size: 200,
            created: '2015-01-14T01:21:56.870',
            links: {
                self: '/uploads/test.png'
            }
        },
        model = uploads.push(file);
    assert.equal(model.url(), '/uploads/test.png');
});

QUnit.test('Model Construct URL', function (assert) {
    var uploads = new config.collections.UploadCollection(),
        model = uploads.push({name: 'test.png'});
    assert.equal(model.url(), '/uploads/test.png');
});
