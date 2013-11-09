/**
 * Project
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

    attributes: {

        name: {
            type: 'string',
            required: true
        },
        hackathon: {
            type: 'string',
            required: true
        },
        summary: {
            type: 'string'
        },
        members: {
            type: 'array'
        },
        information: {
            type: 'text'
        }

    }

};
