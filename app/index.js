const generators = require('yeoman-generator');

module.exports = generators.Base.extend({
  app() {
    this.directory('./', './');
  },
});
