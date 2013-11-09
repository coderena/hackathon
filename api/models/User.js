/**
 * User
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

    attributes: {
        username: {
            type: 'string',
            required: true,
            unique: true
        },
        preferredName: {
            type: 'string'
        },
        photoUrl: {
            type: 'string'
        },
        phone: {
            type: 'string'
        },
        extention: {
            type: 'string'
        },
        mobile: {
            type: 'string'
        },
        cube: {
            type: 'string'
        },
        manager: {
            type: 'string'
        },
        department: {
            type: 'string'
        },
        address: {
            type: 'string'
        }

    }

};
