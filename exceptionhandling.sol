pragma solidity ^0.6.10;

contract ExceptionHandling {
    mapping(address=>uint256)public balanceReceived;
    
    function receivemoney()public payable{
        assert(balanceReceived[msg.sender]+msg.value>=balanceReceived[msg.sender]);
        balanceReceived[msg.sender]+=msg.value;
    }
    
    function withdrawmoney(uint256 amount, address payable to)public{
        require(amount<=balanceReceived[msg.sender],"You do not have sufficient money");
        assert(balanceReceived[msg.sender]>=balanceReceived[msg.sender]-amount);
        balanceReceived[msg.sender]-=amount;
        to.transfer(amount);
    }
}
