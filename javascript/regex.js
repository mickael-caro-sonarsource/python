function getBitbucketcloudOwner() {
    var repoUri = 'https://bitbucket.org/mickaelcaro_/sonarcloudtest';
    var regexp = '\\/(\\w*\\W*)\\/[^\\/]*$';
    var match = repoUri.match(regexp);
    console.log(match);
}
getBitbucketcloudOwner();
