pragma solidity ^0.6.10 ;

contract Newconcepts{
    
    /** mapping introduction **/
    mapping(uint256=>bool)public mymappings;
    mapping(address=>bool)public myaddmappings;
    
    
    function setmap(uint256 _index)public{
        mymappings[_index]=true;
    }
    function setaddmap()public payable{
    myaddmappings[msg.sender]=true;
    }
  
  /**Sending money to the smart contract through mapping and also withdrwaing money through mapping**/
  
  mapping(address=>uint256)public balanceReceived;
  
  function sendmoney()public payable{
      balanceReceived[msg.sender]+=msg.value;
  }
  function withdrawmoney(address payable _To, uint256 _amount)public{
     
      balanceReceived[msg.sender]-=_amount;
      _To.transfer(_amount);
  }
  function getbalance()public view returns(uint256){
      return address(this).balance;
  }
}
