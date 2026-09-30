# Security and permissions

## Camera and image data

Production image streams can contain operational or personal information depending on camera placement.

Controls should include:

- camera field-of-view minimization
- image-retention policy
- access restrictions
- encryption in transit
- restricted access to saved frames
- deletion rules for review images

## Model service

The inference API should use authentication when exposed outside a trusted local network.

## Edge deployment

For sensitive environments, inference can run locally so raw images do not leave the site.

## Model artefacts

Model checkpoints should be versioned and write access restricted.

A production release should record:

- model version
- class configuration
- confidence policy
- training dataset version
- evaluation result
