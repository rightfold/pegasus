'use strict';

exports.conj = function(a) {
  return function(b) {
    return a && b;
  };
};
