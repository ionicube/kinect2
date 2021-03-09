{
  'targets': [
    {
      "target_name": "kinect2",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "src/kinect2.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "$(KINECTSDK20_DIR)\\inc"
      ],
      "conditions" : [
      	["target_arch=='ia32'", {
         "libraries": [ "-l$(KINECTSDK20_DIR)\\lib\\x86\\kinect20.lib" ]
        }],
        ["target_arch=='x64'", {
          "libraries": [ "-l$(KINECTSDK20_DIR)\\lib\\x64\\kinect20.lib" ]
        }]
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
