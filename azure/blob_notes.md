# BLOB NOTES

## Blob Storage

Blob storage is not very heirarchical. It is a place where you can just dump everything. Like you might dump all your laundry on your bed.

The bed is the container. You can have as many containers as you want in Blob storage.

To make containers, you need a storage account.

Resource Group > Storage Account > Container > Blob Files

There is no provision for folder organisation within containers. You will need to create multiple containers. There are different ways to organise, for example, you might put all the images in one container.

## Creating Blob

Three ways:
1. Azure Portal
2. Azure CLI
3. Azure PowerShell

### Azure CLI

Every command for Azure CLI starts with "az"

We are essentially accessing an API, so when we log in, it outputs the login-subscription details as JSON.

NB: DO NOT SHARE THIS INFO PUBLICALLY. SECURITY RISK!

Creating storage account returns more JSON. You cannot use hyphons in the storage account name, will return error. Numbers and lowercase only.



* az login
* Create storage account
  ```
  az storage account create --name tech241peterstorage --resource-group tech241 --location uksouth --sku Standard_LRS
  ```
* List all storage accounts to check it worked
  ```
  az storage account list --resource-group tech241
  ```
  (NB: There is a better way to format this. See below:)
  ```
  az storage account list --resource-group tech241 --query "[].{Name:name, Location:location, Kind:kind}" --output table
  ```
    * There are lots of parameters you can set in the above, have a look into that.
* Create a container
    ```
    az storage container create \ --account-name tech241peterstorage \ --name testcontainer
    ```
    * The backslash allows you to break the command up into multiple lines, to make it easier for you to read as a human.
    * Tip: try taking backslashes out if you have a command that looks right but isn't working.
    * For example, this command in one line:
  ```
  az storage container create --account-name tech241peterstorage --name testcontainer
  ```
* Upload a blob
```
  az storage blob upload \
 --account-name tech241peterstorage \
  --container-name testcontainer \
   --name myFile.txt \
    --file myFile.txt \
     --auth-mode login
```
*  file = the file on the computer. name = File name you want to give it when it's uploaded
* Check the blob has uploaded by listing blobs:
  ```
  az storage blob list \
   --account-name tech241peterstorage \
    --container-name testcontainer \
     --output table \
     --auth-mode login
  ```   
     * note: blob tiers have different costs. Which one you choose depends on how quickly you want access to the blob and how often you will need access it.
* Change the blob from private to public
  * Azure > Storage Account > Data Storage> Containers
  * Select container
  * Change access will no longer be greyed out
  * Change to read access for blob
  * Click on the container, then on the blob, then copy link. Paste into new tab to check it worked.

### Research Task 5.1a

1. What are blobs?
   * Blobs are Binary Large OBjects. A blob is a storage option for data stored in binary format.
2. Blob System vs Heirarchical Storage found in Windows/Linux/MacOS?
   * Blobs are used to store vast amounts of unstructured data. They are not heirarchical.
3. Adv of Blob?
   * Blob has better scalability than file systems.
   * Data stored in Blobs has better availability.
   * Blob is more cost effective. Pay for what you use, and there are different tiers of storage.
   * Blobs have good security. They are encrypted at rest and in transit. There are many features in Azure that further boost blob security.
   * Blobs integrate with other Azure services.
4. Disadv of Blob?
   * Limited direct querying capability. It's not ideal to be directly querying blobs as they are unstructured by nature. There are Azure services to help with this though
   * Blobs do not support structured data. SQL database would be better for that.
   * Blob might cause performance issues if it has to deal with a lot of small read/write operations.
5. Different tiers of Blob storage?
   * Hot Access Tier: Optimized for frequently accessed data, providing low-latency access and higher storage costs compared to other tiers.
   * Cool Access Tier: Designed for infrequently accessed data, offering lower storage costs but with slightly higher access costs and higher data retrieval latency.
   * Archive Access Tier: Intended for long-term archival storage, with the lowest storage costs but higher access costs and longer retrieval times (hours) for accessing the data.
6. Relation of different parts of blob?
7. resource group>storage account>container>blob
---
### Research Task 5.1b: Redundancy
**Redundancy** = Having copies of things that aren't always necessary. Backup copies of things in certain places - so that in case of disaster, you can fall back on these redundancies.

Redundancy has to be set when creating storage account.

1. LRS (Locally Redundant Storage): LRS stores multiple copies of your data within a single data center, providing a cost-effective redundancy option with high durability but without geographic replication for disaster recovery.

2. ZRS (Zone-Redundant Storage): ZRS replicates your data synchronously across multiple availability zones within a region, offering higher availability and durability than LRS by protecting against data center failures within a region.

3. GRS (Geo-Redundant Storage): GRS replicates your data asynchronously to a secondary region, providing additional data durability and availability in the event of a regional disaster or primary region unavailability.

4. RA-GRS (Read-Access Geo-Redundant Storage): RA-GRS provides the same features as GRS but with the added capability of read access to the replicated data in the secondary region, enabling you to read your data even if the primary region is unavailable.

5. GZRS (Geo-Zone-Redundant Storage): GZRS combines the benefits of ZRS and GRS by synchronously replicating data across multiple availability zones within the primary region and asynchronously replicating it to a secondary region for enhanced durability and availability.

6. RA-GZRS (Read-Access Geo-Zone-Redundant Storage): RA-GZRS combines the features of RA-GRS and GZRS, providing synchronous replication across availability zones in the primary region, asynchronous replication to a secondary region, and read access to the replicated data in both regions for maximum durability, availability, and data access capabilities.