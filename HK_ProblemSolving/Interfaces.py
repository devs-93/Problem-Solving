class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n+1):
            if int(n % i) == 0:
                sum = sum + i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

/opt/mapr/hue/hue-3.12.0/bin/hue.sh runcpserver start
/opt/mapr/hive/hive-2.1/bin/hive --service hiveserver2 start
/opt/mapr/hadoop/hadoop-2.7.0/sbin/httpfs.sh start




/opt/mapr/server/configure.sh -C mapr0:7222,mapr1:7222,mapr2:7222 -Z mapr0:5181,mapr1:5181,mapr2:5181 -u ie -N central.ie.datalytix
/opt/mapr/server/configure.sh -C ie1:7222,ie2:7222,ie3:7222 , -Z ie1:5181,ie2:5181,ie3:5181 -u datalytics -N staging.jet.analytics


/opt/mapr/server/configure.sh -C ie1:7222,ie2:7222,ie3:7222  -Z ie1:5181,ie2:5181,ie3:5181  -D /dev/sda4 -u datalytics -N staging.jet.analytics


/opt/mapr/server/configure.sh -C ie1:7222,ie2:7222,ie3:7222 , -Z ie1:5181,ie2:5181,ie3:5181  -D /dev/sda4 -u datalytics -N staging.jet.analytics



export JAVA_HOME=/opt/jdk1.8.0_101
export JRE_HOME=/opt/jdk1.8.0_101/jre
export PATH=$PATH:/opt/jdk1.8.0_101/bin:/opt/jdk1.8.0_101/jre/bin
