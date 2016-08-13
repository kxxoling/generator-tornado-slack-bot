const generators = require('yeoman-generator');

module.exports = generators.Base.extend({
  app() {
    this.directory(
      this.templatePath('src'),
      './'
    );
    this.copy(this.templatePath('dotfiles', '_editorconfig'), '.editorconfig');
    this.copy(this.templatePath('dotfiles', '_gitignore'), '.gitignore');
  },
});
