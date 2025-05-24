import argostranslate.package, argostranslate.translate

# Tải model English -> Vietnamese
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = list(
    filter(lambda x: x.from_code == "en" and x.to_code == "vi", available_packages)
)[0]

download_path = package_to_install.download()
argostranslate.package.install_from_path(download_path)

print("✅ Installed English → Vietnamese model successfully!")