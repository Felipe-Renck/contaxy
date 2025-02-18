<!-- markdownlint-disable -->

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `contaxy.clients.components`




**Global Variables**
---------------
- **CORE_EXTENSION_ID**


---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ComponentClient`




<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(session: Session)
```






---

#### <kbd>property</kbd> global_state





---

#### <kbd>property</kbd> request_state







---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_auth_manager`

```python
get_auth_manager() → AuthOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_extension_manager`

```python
get_extension_manager() → ExtensionOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_file_manager`

```python
get_file_manager(extension_id: Optional[str] = 'core') → FileOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_job_manager`

```python
get_job_manager(extension_id: Optional[str] = 'core') → JobOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_json_db_manager`

```python
get_json_db_manager() → JsonDocumentOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_project_manager`

```python
get_project_manager() → ProjectOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_seed_manager`

```python
get_seed_manager() → SeedOperations
```





---

<a href="https://github.com/ml-tooling/contaxy/blob/main/backend/src/contaxy/clients/components.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_system_manager`

```python
get_system_manager() → SystemOperations
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
