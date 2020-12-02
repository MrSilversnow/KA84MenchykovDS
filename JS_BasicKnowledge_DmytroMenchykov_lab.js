//Менчиков Дмитро, КА-84
// If you want to check other functions, you can use function tasksTest().
function tasksTest(){
  const assert = require('assert');

  // Task №1. Test.
  assert.deepEqual(filter_list([1,2,'a','b']), [1,2]);
  assert.deepEqual(filter_list([1,'a','b',0,15]), [1,0,15]);
  assert.deepEqual(filter_list([1,2,'aasf','1','123',123]), [1,2,123]);
  console.log('Test №1 passed');

  // Task №2. Test.
  assert.equal(first_non_repeating_letter('stress'), 't');
  assert.equal(first_non_repeating_letter('sTreSS'), 'T');
  assert.equal(first_non_repeating_letter('SS'), '');
  console.log('Test №2 passed');

  // Task №3. Test.
  assert.equal(digital_root(16), 7);
  assert.equal(digital_root(942), 6);
  assert.equal(digital_root(132189), 6);
  assert.equal(digital_root(493193), 2);
  console.log('Test №3 passed');

  // Task №4. Test.
  assert.equal(target_pairs(5, [1,3,6,2,2,0,4,5]), 4);
  assert.equal(target_pairs(6, [1,2,5,6,3,0,4,5]), 4);
  console.log('Test №4 passed');

  // Task №5. Test.
  assert.equal(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"),
                  "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)")
  console.log('Test №5 passed');

  // ExtraTask №1. Test.
  assert.equal(nextBigger(9), -1);
  assert.equal(nextBigger(12), 21);
  assert.equal(nextBigger(513), 531);
  assert.equal(nextBigger(531), -1);
  assert.equal(nextBigger(2017), 2071);
  assert.equal(nextBigger(111), -1);
  assert.equal(nextBigger(2431), 3124);
  console.log('ExtraTest №1 passed');

  // ExtraTask №2. Test.
  assert.equal(IP_convert(2149583361), '128.32.10.1');
  assert.equal(IP_convert(32), '0.0.0.32');
  assert.equal(IP_convert(0), '0.0.0.0');
  console.log('ExtraTest №2 passed');
}

// Task №1
function filter_list(lst){
    return lst.filter(element => Number.isInteger(element));
}

// Task №2
function first_non_repeating_letter(str){
  for(let i = 0; i < str.length-1; ++i){
    low_str = str.toLowerCase().slice(i+1)
    low_sym = str.toLowerCase()[i]
    if(!low_str.includes(low_sym))
      return str[i]
  }
  return ""
}

// Task №3
function digital_root(n){
  while(n >= 10){
    let res = 0
    n = String(n)
    for(indx in n)
      res += Number(n[indx])
    n = res
  }
  return n
}

// Task №4
function target_pairs(target, arr){
  let pairs = 0
  for(let i=0; i<arr.length; ++i)
    for(let j=i+1; j<arr.length; ++j){
      if(arr[i]+arr[j]==target)
        ++pairs
    }
  return pairs
}

// Task №5
function meeting(str){
  str = str.toUpperCase().split(';')
  let tmp = []
  for(let i=0; i<str.length; ++i){
    let tpl = str[i].split(':')
    tmp.push(`(${tpl[1]}, ${tpl[0]})`)
  }
  tmp.sort()
  let res = ''
  for(indx in tmp)
    res += tmp[indx]
  return res
}

// ExtraTask №1
function nextBigger(num){
  // It's a really slow function, but the task isn't contain any speed limits.
  if(String(num)!=String(String(num).split('').sort().reverse()).replace(/,/g,'')){
    function str_statistic(str){
      let numbers = Object()
      for(indx in str){
        if(numbers[str[indx]])
          numbers[str[indx]] += 1
        else
          numbers[str[indx]] = 1
      }
      return numbers
    }
    function obj_equal(obj_1, obj_2){
      return String(Object.entries(obj_1).sort()) == String(Object.entries(obj_2).sort())
    }
    num_map = str_statistic(String(num))
    res_map = Object()
    while(!obj_equal(num_map, res_map)){
      num += 1
      res_map = str_statistic(String(num))
    }
  }
  else{
    num = -1
  }
  return num
}

// ExtraTask №2
function IP_convert(uns){
  uns = Number(uns).toString(2)
  while(uns.length < 32){
    uns = '0' + uns
  }
  first_octet = String(parseInt(uns.slice(0,8), 2))
  second_octet = String(parseInt(uns.slice(8,16), 2))
  third_octet = String(parseInt(uns.slice(16,24), 2))
  fourth_octet = String(parseInt(uns.slice(24,32), 2))
  return first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
}
