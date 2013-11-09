/**
 * Hackathon
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

    attributes: {

        name: {
            type: 'string',
            required: true,
            unique: true
        },
        template: {
            type: 'string',
            required: true,
            defaultsTo: 'default'
        },
        slug: {
            type: 'string',
            unique: true
        },
        cover: {
            type: 'string'
        },
        start: {
            type: 'datetime'
        },
        end: {
            type: 'datetime'
        },
        instruction: {
            type: 'text'
        },
        admins: {
            type: 'array'
        }


    }

};
