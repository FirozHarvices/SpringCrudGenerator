imports = """
import com.fasterxml.jackson.annotation.JsonBackReference;
import org.springframework.data.annotation.CreatedBy;
import org.spr ingframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedBy;
import org.springframework.data.annotation.LastModifiedDate;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;
import java.time.LocalDate;
"""

klass = """
@Entity
@Table(name = "${table}")
public class ${class} extends BaseModel"""

column = """
private ${type} ${column.var};
"""

joinColumnId = """
  @Column(name = "${join}_id", insertable = false, updatable = false)
  private Long ${join.camel.fc}Id;

"""
notNull = """@NotNull(message = "${join.camel.fc} is required!")"""

template = """
package ${package}.model;
${imports}
//Auto Generated By SpringCrudGenerator2.0
${class} {
${columns}
}
"""