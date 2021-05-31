#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;
uniform vec3 global_light_pos;

out vec3 light_pos;

out vec2 uv;
out vec3 pos;
out vec3 normal;

void main() {
    mat4 view_model = view * model;
    gl_Position = proj * view_model * vec4(in_position, 1.0);
    pos = vec3(view_model * vec4(in_position, 1.0));
    uv = in_texcoord_0;
    mat3 view_normal = inverse(transpose(mat3(view_model)));
    normal  = mat3(transpose(inverse(view_model))) * in_normal;
    light_pos = vec3(view * vec4(global_light_pos, 1.0));
}

#elif defined FRAGMENT_SHADER

in vec2 uv;
in vec3 normal;
in vec3 pos;
in vec3 light_pos;

uniform sampler2D image;
uniform vec3 light_color;

out vec4 out_color;

void main() {
    vec3 ambient = 0.2 * light_color;
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - pos);
    float diff = max(dot(norm, light_dir), 0.0);
    vec3 diffuse = diff * light_color;
    out_color = vec4((ambient + diffuse), 1.0) * texture(image, uv);
}
#endif
