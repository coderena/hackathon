/**
 * Global adapter config
 */

module.exports.adapters = {

    default: 'mongo',

    mongo: {
        module   : 'sails-mongo',
        host     : 'localhost',
        port     : 27017,
        user     : '',
        password : '',
        database : 'hackathon'
    }
};