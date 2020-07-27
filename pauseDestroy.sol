pragma solidity ^0.6.10;

contract testcontract{
    address public owner;
    bool public pause=false;
    constructor()public{
        owner=msg.sender;
    }
    
    function sendMoney()public payable{

    }
    
    
    function withdrawMoney(address payable _to)public{
        require(msg.sender==owner,'You are not the owner so this transaction cannot be processed');
        require(!pause,'This smart contract is paused');
        _to.transfer(address(this).balance);
    }
    function setpause(bool _pause)public{
        require(owner==msg.sender);
        pause=_pause;
    }
  
  function destroy(address payable _To)public{
      require(msg.sender==owner);
      selfdestruct(_To);
  }
}
