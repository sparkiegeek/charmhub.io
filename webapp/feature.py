# flake8: noqa

# TODO This list of featured charms is random Once the import is complete we
# should include the actual list of charms.
# And once the API provides featured charms then we should remove this code
FEATURED_CHARMS = [
    {
        "name": "prometheus",
        "display_name": "Prometheus",
        "summary": "Prometheus for Kubernetes clusters",
        "publisher": "charmcraft",
        "icon": "https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_64,h_64/https://api.snapcraft.io/api/v1/media/download/charm_ZhkY5AmM2Gncryt3xMkejF4Wyn8lZMSL_icon__dba76c5b8378a96bb711093e2cf55a2dd098f938e9aff22e13403a8e28b87548.png",
        "platform": "kubernetes",
    },
    # {
    #     "name": "postgresql",
    #     "display_name": "PostgreSQL",
    #     "summary": "PostgreSQL charm for Kubernetes deployments.",
    #     "publisher": "postgresql-charmers",
    #     "icon": "https://api.jujucharms.com/charmstore/v5/~postgresql-charmers/postgresql-k8s-5/icon.svg",
    #     "platform": "kubernetes",
    # },
    {
        "name": "discourse",
        "display_name": "Discourse",
        "summary": "Discourse bundled for juju-k8s deployment",
        "publisher": "discourse-charmers",
        "icon": "https://api.jujucharms.com/charmstore/v5/~discourse-charmers/discourse-k8s-7/icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "elasticsearch",
        "display_name": "Elasticsearch",
        "summary": "Elasticsearch is the distributed search and analytics engine.",
        "publisher": "charmcraft",
        "icon": "https://api.jujucharms.com/charmstore/v5/~charmcraft/elasticsearch-0/icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "mattermost",
        "display_name": "Mattermost",
        "summary": "Mattermost charm",
        "publisher": "mattermost-charmers",
        "icon": "https://api.jujucharms.com/charmstore/v5/~mattermost-charmers/mattermost-9/icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "grafana",
        "display_name": "Grafana",
        "summary": "Data vizualization for the charmed LMA stack",
        "publisher": "charmcraft",
        "icon": "https://api.jujucharms.com/charmstore/v5/~charmcraft/grafana-0/icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "wordpress",
        "display_name": "Wordpress",
        "summary": "WordPress is a full featured web blogging tool, this charm deploys it.",
        "publisher": "charmcraft",
        "icon": "https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_64,h_64/https://api.snapcraft.io/api/v1/media/download/charm_gShnGJOjDv34a5pTsYaJB70YMfkfxLGh_icon__418ffcecc722f138690d719f8ea15f478a0a59a72b9c6425fea762b46c1aef4c.png",
        "platform": "linux",
    },
    {
        "name": "alertmanager",
        "display_name": "AlertManager",
        "summary": "Alert management for charmed LMA stack",
        "publisher": "charmcraft",
        "icon": "https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_60,h_60/https://assets.ubuntu.com/v1/be6eb412-snapcraft-missing-icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "cassandra",
        "display_name": "Cassandra",
        "summary": "Distributed storage system for structured data",
        "publisher": "narindergupta",
        "icon": "https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_64,h_64/https://api.snapcraft.io/api/v1/media/download/charm_tWJQBVwAkpEVNJQaqV01zljMjnTk3Wpl_icon__c54853d543881d105dde58c94baf1b36cb4054b836c3246a6b02bb056867a23e.png",
        "platform": "linux",
    },
    {
        "name": "mongodb",
        "display_name": "MongoDB",
        "summary": "An open-source document database, and the leading NoSQL database",
        "publisher": "charmcraft",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_Jfd56ZWJ9IaNHuPjXVLP9d9Xa2XMTSKp_icon__dcd4f86fe38ca430e0e2b221c6ea949af2e04778fae4b4b73658dccc09260714.png",
        "platform": "linux",
    },
    {
        "name": "zookeeper",
        "display_name": "Zookeeper",
        "summary": "Zookeeper from Apache Bigtop",
        "publisher": "narindergupta",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_YKzuWQUoiRwOS6A7T2qjokoj69lJuur9_icon__56c07857177931a872c5c9b8057c80ca98824e557880a43271799758fe5432cf.png",
        "platform": "linux",
    },
    {
        "name": "kafka",
        "display_name": "Kafka",
        "summary": "Kafka from Apache Bigtop",
        "publisher": "charmed-osm",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_WiX6gKBjDZF04gEoTMv2kSNYXvnB2xeF_icon__2618761341037f5e1700e2d6c77178276954840a02dbd62465e22bf1d9a1e904.png",
        "platform": "linux",
    },
    {
        "name": "mysql",
        "display_name": "mysql",
        "summary": "MySQL is a fast, stable and true multi-user, multi-threaded SQL database",
        "publisher": "is",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_F8CtvgcznoeRSupRrY2uEa67oQtBTF7x_icon__69ddfd46786f49d8e952d56c4809e7c08741f732bd000d6faa0970048e2a33c8.png",
        "platform": "linux",
    },
    {
        "name": "mariadb",
        "display_name": "MariaDB",
        "summary": "Popular, enhanced, drop-in replacement for MySQL",
        "publisher": "osm",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_tNiFc3ACzOzO0BUJOTSxeAxVue7rUN1c_icon__62946c7f73307231d38af66f8253f86199df01fdfcaa5547b1b4f5d59b5c0d20.png",
        "platform": "linux",
    },
    {
        "name": "jenkins-agent",
        "display_name": "Jenkins Agent ",
        "summary": "jenkins-agent operator charm",
        "publisher": "jenkins-ci-charmers",
        "icon": "https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_60,h_60/https://assets.ubuntu.com/v1/be6eb412-snapcraft-missing-icon.svg",
        "platform": "kubernetes",
    },
    {
        "name": "telegraf",
        "display_name": "Telegraf",
        "summary": "The plugin-driven server agent for collecting & reporting metrics.",
        "publisher": "telegraf-charmers",
        "icon": "https://api.snapcraft.io/api/v1/media/download/charm_WUIj9keqJBgo29PCR0i7SKV1qXypEsOb_icon__d1ae3bdb493b3ad1bb6aeea483ff601b26cbf1915c3478bad9f5f53b79a729fd.png",
        "platform": "linux",
    },
]
