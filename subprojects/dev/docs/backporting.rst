`Meson version 1.1 <https://mesonbuild.com/Release-notes-for-1-1-0.html>`_

There are a number of concerns that would need to be addressed
to backport OZI to Meson 1.0 and Meson 0.X releases.

* The use of the 'in' operator on string options is not supported prior to 1.0
* The use of the 'not in' operator on string options is not supported prior to 1.0
* Support for reading options from meson.options was added in 1.1
* Use of Feature.enable_auto_if() is not supported prior to 1.1
* Use of FeatureOption.enable_if() is not supported prior to 1.1
* Use of FeatureOption.disable_if() is not supported prior to 1.1
* Use of fs.copyfile() is not supported prior to 0.64

I personally do not see much point in supporting Meson's prior versions.