/**
 * UserController
 *
 * @module      :: Controller
 * @description	:: A set of functions called `actions`.
 *
 *                 Actions contain code telling Sails how to respond to a certain type of request.
 *                 (i.e. do stuff, then send some JSON, show an HTML page, or redirect to another URL)
 *
 *                 You can configure the blueprint URLs which trigger these actions (`config/controllers.js`)
 *                 and/or override them with custom routes (`config/routes.js`)
 *
 *                 NOTE: The code you write here supports both HTTP and Socket.io automatically.
 *
 * @docs        :: http://sailsjs.org/#!documentation/controllers
 */

var ldap = require('ldapjs');

// should move this to configuration file
var EMAIL_SUFFIX = '@juniper.net';


module.exports = {

    login: function(req, res) {
        var client = ldap.createClient({
            url: 'ldap://ldap.jnpr.net'
        });
        if (req.method === 'GET') {
            return res.view('user/login');
        }

        var username = req.body.username;
        var password = req.body.password;
        var email = username;
        var referer = req.header['Referer'] || '/';

        if (username.indexOf(EMAIL_SUFFIX) < 0) {
            email = username + EMAIL_SUFFIX;
        }

        client.bind(email, password, function(err) {
            if (err) {
                req.session.messages = 'Login failed. Please try again.';
                return res.redirect('/login');
            }

            req.session.username = username;
            User.findOneByUsername(username).done(function(err, user) {
                if (err) {
                    User.create({username: username}).done(function(err, user) {
                        if (err) {
                            req.session.messages = 'Failed to create user.';
                            return res.redirect('/login');
                        }
                        req.session.user = user;
                        return res.redirect(referer);
                    });
                } else {
                    req.session.user = user;
                    return res.redirect(referer);
                }
            });

        });
    },



    /**
     * Overrides for the settings in `config/controllers.js`
     * (specific to UserController)
     */
    _config: {}


};
