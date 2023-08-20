# rl-string-helper
`RLStringHelper` is designed specifically for use with Medium.com parser as string markup helper. The basic idea is to apply multiple markups, multiple replacements, to the same character positions. Also adapts all characters to UTF-16 encoding. See tests for more information.

## TODO:
 - Implement the 'adoption agency algorithm' by using positions instead of HTML markups, see as references: https://html.spec.whatwg.org/multipage/parsing.html#adoption-agency-algorithm and https://github.com/html5lib/html5lib-python/blob/3e500bb6e4188/html5lib/html5parser.py#L1408C13-L1408C60
