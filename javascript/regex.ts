function getBitbucketcloudOwner() {
    let repoUri = 'https://bitbucket.org/mickaelcaro_/sonarcloudtest';
    let regexp = '\\/(\\w*\\W*)\\/[^\\/]*$';
    let match = repoUri.match(regexp);
    console.log(match);
  }

  getBitbucketcloudOwner();