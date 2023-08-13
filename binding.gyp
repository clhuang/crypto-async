{
  "targets": [
    {
      "target_name": "binding",
      "sources": [ "binding.c" ]
      'conditions': [
        ['node_shared_openssl=="false"', {
          # so when "node_shared_openssl" is "false", then OpenSSL has been
          # bundled into the node executable. So we need to include the same
          # header files that were used when building node.
          'include_dirs': [
            '<(node_root_dir)/deps/openssl/openssl/include'
          ],
          "conditions" : [
            ["target_arch=='ia32'", {
              "include_dirs": [ "<(node_root_dir)/deps/openssl/config/piii" ]
            }],
            ["target_arch=='x64'", {
              "include_dirs": [ "<(node_root_dir)/deps/openssl/config/k8" ]
            }],
            ["target_arch=='arm'", {
              "include_dirs": [ "<(node_root_dir)/deps/openssl/config/arm" ]
            }]
          ]
        }]
      ]
    },
    {
      "target_name": "copy",
      "type": "none",
      "dependencies": [ "binding" ],
      "copies": [
        {
          'destination': '<(module_root_dir)',
          'files': ['<(module_root_dir)/build/Release/binding.node']
        }
      ]
    }
  ]
}
