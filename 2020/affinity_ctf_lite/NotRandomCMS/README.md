# NotRandomCMS

**Category**: OSINT \
**Point**: 129

Unzipping the file reveals a PHP web app. Since this is an OSINT problem, I
just seached "NotRandomCMS" on GitHub first, which takes us
[here](https://github.com/notrandomcms/notrandomcmsv1). Looking at the commit
history, we see
[this commit](https://github.com/notrandomcms/notrandomcmsv1/commit/6cdec47e7b78394095de5c8856fd67e2a9b6410c)
called "Remove secret files". Looking at
[config/web.php](https://github.com/notrandomcms/notrandomcmsv1/blob/bc757ed02ff3927ab7ce0298be1099a4ca81dbe0/config/web.php)
from this commit, we see:
```
    // !!! insert a secret key in the following (if it is empty) - this is required by cookie validation
    'cookieValidationKey' => 'AFFCTF{thisShouldBeASecret!}',
```
