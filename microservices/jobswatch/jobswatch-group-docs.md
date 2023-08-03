# IT Jobswatch Group Task Documentation

## Intro

This task was undertaken as part of DevOps Tech241 Training with Sparta Global. The team members were:

* Henry Paterson
* Parichat Chanket
* Ryan Singh Johal
* Peter Forbes
* Zain Ashfaq
* Mushahid Ali


## Getting app to run on python environment 
**Steps:**

Install dependencies.  

Run tests 

Run the apps 



Blocker: Dependencies missing. Solution: Install them manually, then update the requirements.txt file 

Blocker: Code failing tests. Solution: Alter the parameters of the tests to reflect the newer version of the app. 

Blocker: app.py not running. Solution: newer version of jinja2 did not have Markup, so downgrading Jinja2 solved this. 

Adding Encoding Argument: We encountered another issue with the encoding of the CSV file, as it contains non-standard ASCII characters. To handle this, we added the `encoding='ISO-8859-1'` argument when opening the CSV file. The updated code now looks like this: 

```python 

def data(): 
    with open('Flask/Downloads/ItJobsWatchTop30.csv', encoding='ISO-8859-1') as csv_file: 
        # Rest of the code... 
``` 

Successful Execution: After making these changes, the Flask app successfully reads and processes the CSV file, and the data is displayed correctly in the browser. 

 

 

## Containerising the app 
**Steps:**

Create Image 

Create Container 

While creating the container, we attempted to resolve a file not found error by adding a volume that would mount the missing file into the correct file path on the conta 

Blocker: File Not Found Error. Solution: Update the file path in app.py for the missing file. 

Blocker: Unicode Error. Solution: Specify the encoding of the file after the file path in app.py. 

 

 

## Deploying Container with Kubernetes 

Create Yaml Files 

 

 

```yaml 

--- 
# PersistentVolumeClaim definition 
apiVersion: v1 
kind: PersistentVolumeClaim 
metadata: 
  name: app-pvc 
spec: 
  accessModes: 
    - ReadWriteOnce 
  resources: 
    requests: 
      storage: 256Mi 

``` 
 

This block defines a PersistentVolumeClaim (PVC) named "app-pvc". It requests a storage space of 256Mi and specifies that it can be accessed in ReadWriteOnce mode, meaning it can be mounted by a single node for read and write operations. 

```yaml  

--- 
# Deployment definition 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  name: app-deploy 
spec: 
  selector: 
    matchLabels: 
      app: app 
  replicas: 3 
  template: 
    metadata: 
      labels: 
        app: app 
    spec: 
      containers: 
        - name: app 
          image: parichanket/jobswatch:v1 
          ports: 
            - containerPort: 5000 
          imagePullPolicy: Always 
          volumeMounts: 
            - name: storage 
              mountPath: /data/db 
          resources: 
            limits: 
              memory: 512Mi 
              cpu: "1" 
            requests: 
              memory: 256Mi 
              cpu: "0.2" 
      volumes: 
        - name: storage 
          persistentVolumeClaim: 
            claimName: app-pvc 
``` 

This block defines a Kubernetes Deployment named "app-deploy". It specifies that three replicas (pods) of the app should be created. The pods will be managed by a ReplicaSet that ensures the desired number of replicas is maintained. The pods are based on the template with the "app" label. 

The container specification includes a single container named "app" that uses the image "parichanket/jobswatch:v1". The container exposes port 5000 for communication. It also sets resource limits and requests for the container, specifying that it should use up to 512Mi of memory and 1 CPU unit as a limit, and 256Mi of memory and 0.2 CPU units as a request. Additionally, it mounts the "storage" volume at the path "/data/db" within the container. The "storage" volume is created based on the "app-pvc" PersistentVolumeClaim defined earlier, which ensures data persistence. 

```yaml 

--- 
# Service definition 
apiVersion: v1 
kind: Service 
metadata: 
  name: app-service 
spec: 
  selector: 
    app: app 
  ports: 
    - port: 5000 
      targetPort: 5000 
  type: NodePort 
``` 

This block defines a Kubernetes Service named "app-service". The service selects pods with the "app" label, allowing it to route traffic to the app pods created by the "app-deploy" Deployment. The service exposes port 5000 and forwards incoming traffic to the same port on the app pods. 

Additionally, it specifies that the service type is "NodePort", which means the service will be accessible from outside the cluster on a randomly assigned port on each node. 

Overall, this script sets up a Deployment with three replicas of an app container, each using persistent storage, and exposes the app to the outside world through a Service with NodePort type on port 5000.  

# Combine them into one file 

```yaml 

--- 

apiVersion: v1 

kind: PersistentVolumeClaim 

metadata: 

  name: app-pvc 

spec: 

  accessModes: 

    - ReadWriteOnce 

  resources: 

    requests: 

      storage: 256Mi 

  

--- 

apiVersion: apps/v1 

kind: Deployment 

metadata: 

  name: app-deploy 

spec: 

  selector: 

    matchLabels: 

      app: app 

  replicas: 3 

  template: 

    metadata: 

      labels: 

        app: app 

    spec: 

      containers: 

        - name: app 

          image: parichanket/jobswatch:v1 

          ports: 

            - containerPort: 5000 

          imagePullPolicy: Always 

          volumeMounts: 

            - name: storage 

              mountPath: /data/db 

          resources: 

            limits: 

              memory: 512Mi 

              cpu: "1" 

            requests: 

              memory: 256Mi 

              cpu: "0.2" 

      volumes: 

        - name: storage 

          persistentVolumeClaim: 

            claimName: app-pvc 

  

--- 

apiVersion: v1 

kind: Service 

metadata: 

  name: app-service 

spec: 

  selector: 

    app: app 

  ports: 

    - port: 5000 

      targetPort: 5000 

  type: NodePort 

``` 