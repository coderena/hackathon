module.exports = {
    appName: 'Hackathon',
    site: {
        title: 'Hackathon',
        url: 'https://hackathon.tchen.me',
        description: 'Hackathon - Bring innocation to life',
        keywords: 'innovation, hackathon, startup, idea, thought, experience',
        author: 'Tyr Chen',
        address: "No. 1 Zhongguancun East Road, Beijing, China"


    },

    getPreparedTitle: function() {
        if (this.title) return this.title + ' | ' + this.site.title;
        return this.site.title;
    }


}